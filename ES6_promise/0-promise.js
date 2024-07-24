function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const success = true; // Simulate API call
    if (success) {
      resolve("API response received successfully");
    } else {
      reject(new Error("Failed to receive API response"));
    }
  });
}

export default getResponseFromAPI;
