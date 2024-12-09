import api from '@forge/api';

export const handler = async (event) => {
  console.log('Jira event received:', event);

  // Ejemplo: Crear un ticket en Jira
  const response = await api.asApp().requestJira('/rest/api/3/issue', {
    method: 'POST',
    body: JSON.stringify({
      fields: {
        project: { key: 'YOUR_PROJECT_KEY' },
        summary: 'New automated ticket',
        issuetype: { name: 'Task' },
      },
    }),
    headers: {
      'Content-Type': 'application/json',
    },
  });

  if (response.ok) {
    console.log('Ticket created successfully!');
  } else {
    console.error('Error creating ticket:', response.statusText);
  }
};
