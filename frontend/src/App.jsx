import React from 'react';
import Layout from './components/Layout';
import ChatFeed from './components/ChatFeed';
import ChatInput from './components/ChatInput';
import { useChat } from './hooks/useChat';

function App() {
  const { messages, isLoading, sendMessage, clearChat } = useChat();

  const handleExampleClick = (query) => {
    sendMessage(query);
  };

  const handleFundSelect = (fundName) => {
    // We want the last original user query, ignoring previous "Selected: " messages
    const lastUserMsg = [...messages].reverse().find(m => m.role === 'user' && !m.content.startsWith('Selected:'));
    const query = lastUserMsg ? lastUserMsg.content : `Tell me about ${fundName}`;
    
    sendMessage(query, fundName);
  };

  return (
    <Layout onNewChat={clearChat}>
      <ChatFeed 
        messages={messages} 
        isLoading={isLoading} 
        onExampleClick={handleExampleClick} 
        onFundSelect={handleFundSelect} 
      />
      <ChatInput onSend={sendMessage} isLoading={isLoading} />
    </Layout>
  );
}

export default App;
