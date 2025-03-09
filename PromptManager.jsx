import React, { useState, useEffect } from 'react';

const PromptManager = () => {
  const [prompts, setPrompts] = useState([]);
  const [newPrompt, setNewPrompt] = useState({ name: '', content: {} });

  useEffect(() => {
    fetchPrompts();
  }, []);

  const fetchPrompts = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/v1/prompts/');
      const data = await response.json();
      setPrompts(data);
    } catch (error) {
      console.error('Error fetching prompts:', error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/api/v1/prompts/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newPrompt)
      });
      const data = await response.json();
      setPrompts([...prompts, data]);
      setNewPrompt({ name: '', content: {} });
    } catch (error) {
      console.error('Error saving prompt:', error);
    }
  };

  return (
    <div>
      <h1>Prompt Manager</h1>
      
      {/* Form to add new prompt */}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={newPrompt.name}
          onChange={(e) => setNewPrompt({...newPrompt, name: e.target.value})}
          placeholder="Prompt name"
        />
        <textarea
          value={JSON.stringify(newPrompt.content, null, 2)}
          onChange={(e) => {
            try {
              const content = JSON.parse(e.target.value);
              setNewPrompt({...newPrompt, content});
            } catch (error) {
              // Handle invalid JSON
            }
          }}
          placeholder="Prompt content (JSON)"
        />
        <button type="submit">Save Prompt</button>
      </form>

      {/* Display prompts */}
      <div>
        {prompts.map((prompt) => (
          <div key={prompt.name}>
            <h3>{prompt.name}</h3>
            <pre>{JSON.stringify(prompt.content, null, 2)}</pre>
          </div>
        ))}
      </div>
    </div>
  );
};

export default PromptManager; 