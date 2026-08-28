import { useState, useCallback } from 'react';

export const useChat = () => {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [sessionId, setSessionId] = useState(null);

  const sendMessage = useCallback(async (text, selectedFund = null) => {
    // Optimistically add user message
    if (!selectedFund) {
      setMessages(prev => [...prev, { role: 'user', content: text }]);
    } else {
      setMessages(prev => [...prev, { role: 'user', content: `Selected: ${selectedFund}` }]);
    }
    
    setIsLoading(true);

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          message: text,
          session_id: sessionId,
          selected_fund: selectedFund
        })
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      
      if (!sessionId) {
        setSessionId(data.session_id);
      }

      setMessages(prev => [...prev, {
        role: 'assistant',
        type: data.type,
        content: data.message,
        citation: data.citation,
        educational_link: data.educational_link,
        options: data.options,
        footer: data.footer
      }]);

    } catch (error) {
      console.error("Error sending message:", error);
      setMessages(prev => [...prev, {
        role: 'assistant',
        type: 'error',
        content: "Sorry, I'm having trouble connecting to the server. Please try again."
      }]);
    } finally {
      setIsLoading(false);
    }
  }, [sessionId]);

  const clearChat = () => {
    setMessages([]);
    setSessionId(null);
  };

  return { messages, isLoading, sendMessage, clearChat };
};
