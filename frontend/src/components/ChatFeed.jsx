import React, { useRef, useEffect } from 'react';
import MessageBubble from './MessageBubble';
import WelcomeScreen from './WelcomeScreen';
import { Loader2 } from 'lucide-react';

const ChatFeed = ({ messages, isLoading, onExampleClick, onFundSelect }) => {
  const endRef = useRef(null);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isLoading]);

  if (messages.length === 0) {
    return <WelcomeScreen onExampleClick={onExampleClick} />;
  }

  return (
    <div className="flex-1 overflow-y-auto p-container-padding pb-32">
      <div className="max-w-[800px] mx-auto space-y-stack-lg">
        {messages.map((msg, idx) => (
          <MessageBubble key={idx} msg={msg} onFundSelect={onFundSelect} />
        ))}
        {isLoading && (
          <div className="flex flex-col items-start mt-stack-lg">
            <div className="flex items-end gap-2 mb-1">
              <div className="w-6 h-6 rounded-full bg-primary flex items-center justify-center text-on-primary text-[10px] font-bold">N</div>
              <span className="font-label-md text-label-md text-on-surface-variant">Navi Assistant</span>
            </div>
            <div className="bg-surface-subtle px-4 py-3 rounded-2xl rounded-tl-sm border border-border-light">
              <Loader2 className="w-5 h-5 text-primary animate-spin" />
            </div>
          </div>
        )}
        <div ref={endRef} />
      </div>
    </div>
  );
};

export default ChatFeed;
