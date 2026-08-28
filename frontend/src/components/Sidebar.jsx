import React from 'react';
import { Plus, MessageSquare } from 'lucide-react';

const Sidebar = ({ onNewChat }) => {
  return (
    <aside className="hidden lg:flex w-64 flex-col border-r border-border-light bg-surface-container-low/30 h-[calc(100vh-4rem)] p-stack-md sticky top-16">
      <div className="mb-stack-lg">
        <button 
          onClick={onNewChat}
          className="w-full flex items-center justify-center gap-2 bg-primary text-on-primary px-4 py-2 rounded-lg font-label-md text-label-md hover:bg-surface-tint transition-colors"
        >
          <Plus size={18} />
          New Chat
        </button>
      </div>
      <h2 className="font-label-md text-label-md text-on-surface-variant mb-stack-sm px-2 uppercase tracking-widest">Recent Topics</h2>
      <nav className="flex-1 overflow-y-auto">
        <ul className="space-y-1">
          <li>
            <a className="flex items-center gap-2 px-3 py-2 rounded-md bg-surface-subtle text-primary font-body-md text-body-md truncate" href="#">
              <MessageSquare size={16} />
              Navi Nifty 50 Expense...
            </a>
          </li>
          <li>
            <a className="flex items-center gap-2 px-3 py-2 rounded-md hover:bg-surface-subtle text-on-surface-variant font-body-md text-body-md truncate transition-colors" href="#">
              <MessageSquare size={16} />
              Tax implications of ELSS
            </a>
          </li>
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;
