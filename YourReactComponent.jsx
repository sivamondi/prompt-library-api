// Example using fetch
const savePrompt = async (promptData) => {
  try {
    const response = await fetch('http://localhost:8000/api/v1/prompts/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(promptData)
    });
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
};

// Example using axios
import axios from 'axios';

const getAllPrompts = async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/v1/prompts/');
    return response.data;
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}; 