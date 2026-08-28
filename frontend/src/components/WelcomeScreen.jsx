import React from 'react';
import { Bot, AlertTriangle, Percent, ArrowRightLeft, TrendingUp } from 'lucide-react';

const WelcomeScreen = ({ onExampleClick }) => {
  const exampleQuestions = [
    {
      icon: <Percent size={24} className="text-on-surface-variant group-hover:text-primary" />,
      text: "What is the current expense ratio of the Navi Nifty 50 Index Fund?"
    },
    {
      icon: <ArrowRightLeft size={24} className="text-on-surface-variant group-hover:text-primary" />,
      text: "What is the exit load for Navi ELSS Tax Saver Fund?"
    },
    {
      icon: <TrendingUp size={24} className="text-on-surface-variant group-hover:text-primary" />,
      text: "What is the minimum SIP amount for Navi Midcap 150 Index Fund?"
    }
  ];

  return (
    <div className="flex-1 overflow-y-auto p-4 md:p-8 flex flex-col items-center justify-center">
      <div className="max-w-[800px] w-full flex flex-col items-center text-center mb-4 md:mb-12">
        {/* Bot Icon - hidden on very small screens, smaller on mobile */}
        <div className="w-12 h-12 md:w-16 md:h-16 rounded-full bg-surface-container-low border border-border-light hidden sm:flex items-center justify-center mb-4 md:mb-6 shadow-sm">
          <Bot size={24} className="text-primary md:w-8 md:h-8" />
        </div>
        
        <h2 className="font-headline-md text-headline-md md:font-headline-lg md:text-headline-lg text-on-background mb-3 md:mb-4">How can I help you today?</h2>
        
        {/* Disclaimer */}
        <div className="bg-surface-bright border border-border-light border-l-[3px] border-l-status-warning px-3 py-2 md:px-4 md:py-3 rounded-r-lg max-w-md mx-auto mb-4 md:mb-8 shadow-sm flex items-start gap-2 md:gap-3 text-left">
          <AlertTriangle size={16} className="text-status-warning mt-0.5 min-w-[16px] md:min-w-[20px]" />
          <p className="font-label-sm text-label-sm text-on-surface-variant leading-tight">
            <strong className="text-on-background">Facts-only assistant. No investment advice.</strong> Data provided is for informational purposes only. Consult a financial advisor before making investment decisions.
          </p>
        </div>

        {/* Example Questions */}
        <div className="flex flex-wrap justify-center gap-2 md:gap-4 w-full max-w-2xl mx-auto">
          {exampleQuestions.map((q, i) => (
            <button 
              key={i} 
              onClick={() => onExampleClick(q.text)}
              className="w-[calc(50%-4px)] sm:w-[calc(33.333%-11px)] aspect-square bg-surface-container-lowest border border-border-light p-3 md:p-4 rounded-2xl shadow-sm hover:shadow-md hover:border-primary hover:-translate-y-1 active:scale-95 transition-all group flex flex-col items-center justify-center gap-2 md:gap-3 cursor-pointer"
            >
              <div className="bg-primary/5 group-hover:bg-primary/10 p-2 md:p-3 rounded-full transition-colors duration-300">
                {React.cloneElement(q.icon, { size: 24, className: "text-primary md:w-8 md:h-8" })}
              </div>
              <span className="font-body-sm text-xs md:text-sm text-on-background text-center leading-tight line-clamp-4">{q.text}</span>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};

export default WelcomeScreen;
