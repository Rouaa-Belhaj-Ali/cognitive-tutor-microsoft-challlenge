// src/App.js
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const handleQuestionChange = (e) => {
    setQuestion(e.target.value);
  };

  const handleAskQuestion = async () => {
    try {
      const response = await axios.post('http://localhost:8000/ask', { question });
      setAnswer(response.data.answer);
    } catch (error) {
      console.error('Error fetching answer:', error);
      setAnswer('An error occurred while fetching the answer.');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Cognitive Tutor</h1>
        <textarea
          value={question}
          onChange={handleQuestionChange}
          placeholder="Ask your question here..."
        />
        <button onClick={handleAskQuestion}>Ask</button>
        {answer && (
          <div className="answer">
            <h2>Answer:</h2>
            <p>{answer}</p>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
