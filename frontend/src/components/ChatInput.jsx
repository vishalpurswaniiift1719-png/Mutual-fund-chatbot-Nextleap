import React, { useState } from 'react';
import { Search, Send, ArrowUp } from 'lucide-react';

const ChatInput = ({ onSend, isLoading }) => {
  const [query, setQuery] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (query.trim() && !isLoading) {
      onSend(query.trim());
      setQuery("");
    }
  };

  return (
    <div className="p-container-padding bg-background/90 backdrop-blur-md border-t border-border-light w-full">
      <div className="max-w-[800px] mx-auto">
        <form onSubmit={handleSubmit} className="relative flex items-center">
          <input 
            type="text"
            className="w-full bg-surface-container-lowest border border-border-light rounded-full py-3 pl-4 pr-12 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary font-body-md text-body-md text-on-surface placeholder-on-surface-variant transition-colors shadow-sm"
            placeholder="Ask about fund details, NAV, or expense ratios..." 
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            disabled={isLoading}
          />
          <button 
            type="submit"
            disabled={!query.trim() || isLoading}
            className="absolute right-2 p-2 rounded-full bg-primary text-on-primary hover:bg-surface-tint transition-colors flex items-center justify-center disabled:opacity-50"
          >
            <ArrowUp size={18} />
          </button>
        </form>
        <div className="text-center mt-2">
          <span className="font-label-sm text-label-sm text-on-surface-variant">AI-generated responses. Data as of latest available disclosures.</span>
        </div>
      </div>
    </div>
  );
};

export default ChatInput;
