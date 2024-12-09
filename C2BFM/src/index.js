import api from '@forge/api';

export const handler = async (event) => {
  console.log('Event received:', event);
  return {
    body: `<p>Hello, this is your Project Tree!</p>`,
    headers: {
      'Content-Type': 'text/html'
    }
  };
};
