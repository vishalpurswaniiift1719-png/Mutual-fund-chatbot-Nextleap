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
    <div className="flex-1 overflow-y-auto p-container-padding md:p-8 flex flex-col items-center justify-center">
      <div className="max-w-[800px] w-full flex flex-col items-center text-center mb-12">
        <div className="w-16 h-16 rounded-full bg-surface-container-low border border-border-light flex items-center justify-center mb-6 shadow-sm">
          <Bot size={32} className="text-primary" />
        </div>
        <h2 className="font-headline-lg text-headline-lg text-on-background mb-4">How can I help you today?</h2>
        
        {/* Disclaimer */}
        <div className="bg-surface-bright border border-border-light border-l-[3px] border-l-status-warning px-4 py-3 rounded-r-lg max-w-md mx-auto mb-8 shadow-sm flex items-start gap-3 text-left">
          <AlertTriangle size={20} className="text-status-warning mt-0.5" />
          <p className="font-label-sm text-label-sm text-on-surface-variant">
            <strong className="text-on-background">Facts-only assistant. No investment advice.</strong> Data provided is for informational purposes only. Consult a financial advisor before making investment decisions.
          </p>
        </div>


        {/* Example Questions */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 w-full text-left">
          {exampleQuestions.map((q, i) => (
            <button 
              key={i} 
              onClick={() => onExampleClick(q.text)}
              className="bg-surface-container-lowest border border-border-light p-4 rounded-xl hover:border-primary hover:shadow-sm transition-all group flex flex-col items-start gap-3 h-full"
            >
              {q.icon}
              <span className="font-body-md text-body-md text-on-background">{q.text}</span>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};

export default WelcomeScreen;
