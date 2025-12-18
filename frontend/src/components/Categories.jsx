

import React, { useState, useEffect } from 'react';
import { useNavigate } from "react-router-dom";

const Categories = () => {
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const get_all_categories = async () => {
    setLoading(true);
    setError('');
    try {
      const res = await fetch('http://localhost:5000/api/categories');
      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err.message || res.statusText || 'Failed to fetch categories');
      }
      const data = await res.json();
      setCategories(data);
      return data;
    } catch (e) {
      setError(e.message || 'Error fetching categories');
      return [];
    } finally {
      setLoading(false);
    }
  };

 

  useEffect(() => {
    get_all_categories();
  }, []);

  return (
    <div>
      <h2>Categories</h2> 
      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p style={{ color: 'red' }}>{error}</p>
      ) : (
        <ul>
          {categories.length === 0 ? (
            <li>No categories found</li>
          ) : (
            categories.map((c) => (
              <li key={c.id}>
                <strong>{c.name}</strong>
                {c.description ? ` — ${c.description}` : ''}
              </li>
            ))
          )}
        </ul>
      )}
    </div>
  );
};

export default Categories;