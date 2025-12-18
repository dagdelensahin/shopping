import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";

function CategoriesSave() {

     const navigate = useNavigate();

  const onSave = (category) => {
    fetch('http://localhost:5000/api/categories', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ category }),
    })
    .then((res) => {
      if (!res.ok) {
        return res.json().then((err) => {
          throw new Error(err.message || 'Failed to save categories');
        });
      }
      return res.json();
    })
    .then((data) => {
       navigate("/categories", { replace: true });
    })
    .catch((err) => {
      alert(`Error saving categories: ${err.message}`);
    });
  }

  const handleSave = () => {
      const category = { name, description }; 
      onSave(category);
  };  

    const [description, setDescription] = useState("");
    const [name, setName] = useState("");
  return (
    <form>
      <div>
        <h2>Save Categories</h2>
      </div>
      <div>
      <label>Category Name:</label>
      <input type="text" value={name} onChange={(e) => setName(e.target.value)}  />
      </div>
      <div>
      <label>Category Description:</label>
     <input type="text" value={description} onChange={(e) => setDescription(e.target.value)}  />
      </div>  
      <button type="button" onClick={handleSave}>
        Save Categories
      </button>
    </form>
   );
 
}

 
export default CategoriesSave;
