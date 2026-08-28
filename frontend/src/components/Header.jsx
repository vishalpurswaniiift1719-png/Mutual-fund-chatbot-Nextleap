import React from 'react';
import { Info } from 'lucide-react';

const Header = () => {
  return (
    <header className="fixed top-0 left-0 w-full z-50 flex items-center px-container-padding h-16 bg-background/95 backdrop-blur-sm border-b border-border-light justify-between transition-colors duration-200">
      <div className="flex items-center gap-stack-md">
        <div className="w-8 h-8 rounded-full bg-primary flex items-center justify-center text-on-primary font-bold">
          N
        </div>
        <h1 className="font-headline-md text-headline-md font-bold text-primary">Navi Fund Assistant</h1>
      </div>
      <div className="flex items-center gap-4">
        <button className="p-2 rounded-full hover:bg-surface-subtle text-on-surface-variant transition-colors duration-200">
          <Info size={24} />
        </button>
      </div>
    </header>
  );
};

export default Header;
