import React from 'react';
import Header from './Header';
import Sidebar from './Sidebar';

const Layout = ({ children, onNewChat }) => {
  return (
    <>
      <Header />
      <main className="flex-grow pt-16 flex max-w-[1200px] mx-auto w-full">
        <Sidebar onNewChat={onNewChat} />
        <div className="flex-1 flex flex-col h-[calc(100vh-4rem)] relative">
          {children}
          {/* Footer Component */}
          <footer className="w-full py-4 px-container-padding flex flex-col items-center gap-2 text-center bg-surface-container-low border-t border-status-warning/30">
            <p className="font-label-sm text-label-sm text-on-surface-variant opacity-90">Facts-only assistant. Data as of Oct 2023. Not financial advice.</p>
            <div className="flex gap-4">
              <a className="font-label-sm text-label-sm text-on-surface-variant hover:text-primary transition-colors" href="#">Legal Disclaimer</a>
              <a className="font-label-sm text-label-sm text-on-surface-variant hover:text-primary transition-colors" href="#">Methodology</a>
              <a className="font-label-sm text-label-sm text-on-surface-variant hover:text-primary transition-colors" href="#">Support</a>
            </div>
          </footer>
        </div>
      </main>
    </>
  );
};

export default Layout;
