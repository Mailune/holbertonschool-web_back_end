function getResponseFromAPI() {
  return new Promise((resolve) => {
    const success = true; // Simulate API call
    if (success) {
      resolve('API response received successfully');
    }
  });
}

export default getResponseFromAPI;
