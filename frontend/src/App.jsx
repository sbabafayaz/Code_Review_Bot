import { useState } from 'react';
import './App.css';

function App() {
  const [code, setCode] = useState('');
  const [language, setLanguage] = useState('python');
  const [review, setReview] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleReview = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://127.0.0.1:8000/review', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code, language })
      });
      const data = await response.json();
      setReview(data);
    } catch (err) {
      console.error("Review failed:", err);
      setReview({ error: "Could not connect to backend" });
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2> Code Review Bot</h2>

      <div style={{ marginBottom: 10 }}>
        <label>Select Language: </label>
        <select value={language} onChange={(e) => setLanguage(e.target.value)}>
          <option value="Python">Python</option>
          <option value="JavaScript">JavaScript</option>
          <option value="Java">Java</option>
          <option value="C">C</option>
          <option value="CPP">C++</option>
        </select>
      </div>

      <textarea
        rows={12}
        cols={80}
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Paste your code here..."
        style={{ fontFamily: 'monospace', width: '100%' }}
      />
      <br />
      <button onClick={handleReview} disabled={loading}>
        {loading ? 'Reviewing...' : 'Submit for Review'}
      </button>

      {review && (
        <div style={{ marginTop: 20 }}>
          <h3>Review Results:</h3>

          {/* Gemini Review Section */}
          {review.gemini_review && (
            <div>
              <h4>AI Suggestions:</h4>
              <div
                style={{
                  background: 'black',
                  padding: '10px',
                  borderRadius: '5px',
                  whiteSpace: 'pre-wrap'
                }}
              >
                {review.gemini_review}
              </div>
            </div>
          )}

          {/* Static Issues Section */}
          <div style={{ marginTop: 10 }}>
            <h4>Static Issues:</h4>
            {review.static_issues && review.static_issues.length > 0 ? (
              <ul>
                {review.static_issues.map((issue, index) => (
                  <li key={index}>{issue}</li>
                ))}
              </ul>
            ) : (
              <p>No static issues found.</p>
            )}
          </div>

          {/* Complexity Section */}
          <div style={{ marginTop: 10 }}>
            <h4>Code Complexity:</h4>
            {review.complexity && review.complexity.length > 0 ? (
              <ul>
                {review.complexity.map((item, index) => (
                  <li key={index}>
                    Function <b>{item.name}</b> has complexity {item.complexity}
                  </li>
                ))}
              </ul>
            ) : (
              <p>No complexity data available.</p>
            )}
          </div>

          {/* Security Section */}
          <div style={{ marginTop: 10 }}>
            <h4>Security Review:</h4>
            {review.security && review.security.error ? (
              <p style={{ color: 'red' }}>{review.security.error}</p>
            ) : (
              <p>No security issues reported.</p>
            )}
          </div>

          {/* Fallback for unknown errors */}
          {review.error && (
            <div style={{ color: 'red', marginTop: 10 }}>
              <strong>Error:</strong> {review.error}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
