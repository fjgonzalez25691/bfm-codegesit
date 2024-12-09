import api from '@forge/api';

export const handler = async (event) => {
  console.log('Confluence event received:', event);

  // Ejemplo: Actualizar una página de Confluence
  const pageId = 'YOUR_PAGE_ID';
  const response = await api.asApp().requestConfluence(`/wiki/api/v2/pages/${pageId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      id: pageId,
      title: 'Updated Page Title',
      body: {
        representation: 'storage',
        value: '<p>This is an updated page content!</p>',
      },
      version: {
        number: 2, // Incrementar el número de versión
      },
    }),
  });

  if (response.ok) {
    console.log('Page updated successfully!');
  } else {
    console.error('Error updating page:', response.statusText);
  }
};
