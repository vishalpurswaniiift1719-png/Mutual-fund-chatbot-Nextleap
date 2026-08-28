import React from 'react';
import { CheckCircle2, AlertTriangle, ChevronRight } from 'lucide-react';

const renderTextWithLinks = (text) => {
  if (!text) return null;
  const urlRegex = /(https?:\/\/[^\s]+)/g;
  const parts = text.split(urlRegex);
  return parts.map((part, i) => {
    if (part.match(urlRegex)) {
      // If it ends with a punctuation like ., clean it up
      const cleanUrl = part.replace(/[.,;)]+$/, '');
      const trailing = part.slice(cleanUrl.length);
      return (
        <React.Fragment key={i}>
          <a href={cleanUrl} target="_blank" rel="noopener noreferrer" className="text-secondary hover:underline">
            {cleanUrl}
          </a>
          {trailing}
        </React.Fragment>
      );
    }
    return <span key={i}>{part}</span>;
  });
};

const MessageBubble = ({ msg, onFundSelect }) => {
  const isUser = msg.role === 'user';

  if (isUser) {
    return (
      <div className="flex flex-col items-end mt-stack-lg">
        <div className="bg-surface-container-high text-on-surface px-4 py-3 rounded-2xl rounded-tr-sm max-w-[85%] border border-border-light">
          <p className="font-body-lg text-body-lg whitespace-pre-wrap">{renderTextWithLinks(msg.content)}</p>
        </div>
      </div>
    );
  }

  // Assistant messages
  return (
    <div className="flex flex-col items-start mt-stack-lg w-full">
      <div className="flex items-end gap-2 mb-1">
        <div className="w-6 h-6 rounded-full bg-primary flex items-center justify-center text-on-primary text-[10px] font-bold">N</div>
        <span className="font-label-md text-label-md text-on-surface-variant">Navi Assistant</span>
      </div>

      {msg.type === 'answer' && (
        <div className="bg-surface-subtle text-on-surface px-4 py-4 rounded-2xl rounded-tl-sm max-w-[85%]">
          <p className="font-body-lg text-body-lg mb-stack-md whitespace-pre-wrap">{renderTextWithLinks(msg.content)}</p>
          
          {msg.citation && (
            <div className="bg-background border border-border-light rounded-lg p-3 mt-4 flex flex-col items-start gap-2">
              <div className="flex items-center gap-2">
                <CheckCircle2 size={18} className="text-on-surface-variant" />
                <span className="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider">Source Link</span>
              </div>
              <a href={msg.citation} target="_blank" rel="noopener noreferrer" className="font-label-sm text-label-sm text-secondary hover:underline break-all">
                {msg.citation}
              </a>
            </div>
          )}
        </div>
      )}

      {msg.type === 'refusal' && (
        <div className="bg-surface-subtle text-on-surface px-4 py-3 rounded-2xl rounded-tl-sm max-w-[85%] border-l-2 border-status-warning">
          <p className="font-body-lg text-body-lg mb-2 whitespace-pre-wrap">{renderTextWithLinks(msg.content)}</p>
          {msg.educational_link && (
            <p className="font-body-md text-body-md text-on-surface-variant">
              You may find educational resources here: <a className="text-secondary underline hover:text-secondary-fixed-variant" href={msg.educational_link} target="_blank" rel="noopener noreferrer">SEBI Investor Education</a>
            </p>
          )}
        </div>
      )}
      
      {msg.type === 'privacy_warning' && (
        <div className="bg-surface-subtle text-on-surface px-4 py-3 rounded-2xl rounded-tl-sm max-w-[85%] border-l-2 border-error">
           <div className="flex items-center gap-2 mb-2 text-error">
              <AlertTriangle size={18} />
              <span className="font-bold">Privacy Warning</span>
           </div>
          <p className="font-body-lg text-body-lg whitespace-pre-wrap">{renderTextWithLinks(msg.content)}</p>
        </div>
      )}

      {msg.type === 'error' && (
        <div className="bg-surface-subtle text-on-surface px-4 py-3 rounded-2xl rounded-tl-sm max-w-[85%] border-l-2 border-error">
           <div className="flex items-center gap-2 mb-2 text-error">
              <AlertTriangle size={18} />
              <span className="font-bold">Error</span>
           </div>
          <p className="font-body-lg text-body-lg whitespace-pre-wrap">{renderTextWithLinks(msg.content)}</p>
        </div>
      )}

      {msg.type === 'disambiguation' && (
        <div className="bg-surface-subtle text-on-surface px-4 py-4 rounded-2xl rounded-tl-sm max-w-[85%]">
          <p className="font-body-lg text-body-lg mb-stack-md whitespace-pre-wrap">{renderTextWithLinks(msg.content)}</p>
          {msg.options && (
            <div className="flex flex-col gap-2 mt-4">
              {msg.options.map((opt, idx) => (
                <button 
                  key={idx}
                  onClick={() => onFundSelect(opt.name)}
                  className="flex justify-between items-center bg-background border border-border-light hover:border-primary p-3 rounded-lg text-left transition-colors group"
                >
                  <span className="font-body-md text-body-md text-on-background group-hover:text-primary">{opt.name}</span>
                  <ChevronRight size={16} className="text-on-surface-variant group-hover:text-primary" />
                </button>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default MessageBubble;
