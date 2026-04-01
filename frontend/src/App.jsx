import { useState } from "react";

function App() {
  const [apiStatus, setApiStatus] = useState("Not connected yet...");
  const [loading, setLoading] = useState(false);

  // This function talks to your Flask backend!
  const checkApiHealth = async () => {
    setLoading(true);
    try {
      // We use the environment variable we set up
      const response = await fetch(`${import.meta.env.VITE_API_URL}/health`);
      const data = await response.json();

      // Update the UI with the message from Flask
      setApiStatus(data.message);
    } catch (error) {
      setApiStatus("Error connecting to the API. Is Flask running?");
    }
    setLoading(false);
  };

  return (
    <div
      style={{ padding: "50px", fontFamily: "sans-serif", textAlign: "center" }}
    >
      <h1>⚛️ React + Flask Boilerplate 🌶️</h1>

      <div
        style={{
          margin: "30px 0",
          padding: "20px",
          border: "1px solid #ccc",
          borderRadius: "8px",
        }}
      >
        <h3>API Status:</h3>
        <p
          style={{
            color: apiStatus.includes("Error") ? "red" : "green",
            fontWeight: "bold",
          }}
        >
          {apiStatus}
        </p>
      </div>

      <button
        onClick={checkApiHealth}
        disabled={loading}
        style={{ padding: "10px 20px", fontSize: "16px", cursor: "pointer" }}
      >
        {loading ? "Checking..." : "Ping Flask API"}
      </button>
    </div>
  );
}

export default App;
