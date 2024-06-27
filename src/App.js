import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);

  const handleQuestionChange = (e) => {
    setQuestion(e.target.value);
  };

  const handleAskQuestion = async () => {
    setLoading(true);
    setAnswer('');
    try {
      const response = await axios.post('http://localhost:8000/ask', { question });
      setAnswer(response.data.answer);
    } catch (error) {
      console.error('Error fetching answer:', error);
      setAnswer('An error occurred while fetching the answer.');
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Cognitive Tutor</h1>
        <div className="chat-container">
          <textarea
            value={question}
            onChange={handleQuestionChange}
            placeholder="Ask your question here..."
            className="question-box"
          />
          <button onClick={handleAskQuestion} className="ask-button" disabled={loading}>
            {loading ? 'Loading...' : 'Ask'}
          </button>
        </div>
        {answer && (
          <div className="answer fade-in">
            <h2>Answer:</h2>
            <p>{answer}</p>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
