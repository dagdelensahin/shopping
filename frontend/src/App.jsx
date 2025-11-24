import React, { useState } from 'react'

export default function App() {
  const [message, setMessage] = useState(null)
  const [loading, setLoading] = useState(false)

  async function fetchGreeting() {
    setLoading(true)
    try {
      const res = await fetch('http://localhost:5000/api/hello?name=React')
      const data = await res.json()
      setMessage(data.message)
    } catch (err) {
      setMessage('Error: ' + err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <header>
        <h1>Shopping (React UI)</h1>
      </header>
      <main>
        <p>This is a minimal React frontend scaffold. Connect it to the Python backend as needed.</p>

        <div style={{marginTop: '1rem'}}>
          <button onClick={fetchGreeting} disabled={loading}>
            {loading ? 'Loading...' : 'Fetch Greeting from API'}
          </button>
          {message && (
            <div style={{marginTop: '0.75rem'}}>
              <strong>API response:</strong>
              <div>{message}</div>
            </div>
          )}
        </div>
      </main>
    </div>
  )
}
