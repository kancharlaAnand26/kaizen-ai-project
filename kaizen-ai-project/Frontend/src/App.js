import React, { useState } from 'react';
import Viewer3D from './components/Viewer3diewer3D';
import './App.css';

function App() {
  const [inputValue, setInputValue] = useState('');
  const [chatHistory, setChatHistory] = useState([
    { sender: 'bot', text: 'Hello! I am your KAIZEN-AI assistant. How can I help you with the Meidensha equipment today?' }
  ]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!inputValue.trim()) return;

    const userMessage = { sender: 'user', text: inputValue };
    const newChatHistory = [...chatHistory, userMessage];
    setChatHistory(newChatHistory);
    setInputValue('');

    try {
      // NOTE: Ensure your backend is running on http://127.0.0.1:8000
      const response = await fetch('http://127.0.0.1:8000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: inputValue }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      const botMessage = { sender: 'bot', text: data.answer };
      setChatHistory([...newChatHistory, botMessage]);

    } catch (error) {
      console.error("Fetch error:", error);
      const errorMessage = { sender: 'bot', text: 'Sorry, I am having trouble connecting to the server.' };
      setChatHistory([...newChatHistory, errorMessage]);
    }
  };

  return (
    <div className="app-container">
      <div className="viewer-container">
        <Viewer3D />
      </div>
      <div className="chat-container">
        <h1>KAIZEN-AI Assistant</h1>
        <div className="chat-window">
          {chatHistory.map((message, index) => (
            <div key={index} className={`message ${message.sender}`}>
              {message.text}
            </div>
          ))}
        </div>
        <form onSubmit={handleSubmit} className="chat-input-form">
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder="Ask about a procedure or part..."
          />
          <button type="submit">Send</button>
        </form>
      </div>
    </div>
  );
}

export default App;