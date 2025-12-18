import React from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Dashboard from './components/Dashboard';
import Login from "./components/Login";
import Categories from './components/Categories';
import CategoriesSave from './components/CategoriesSave';

export default function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/categories" element={<Categories />} />
        <Route path="/categories/save" element={<CategoriesSave />} />
        <Route path="*" element={<h2>404: Page Not Found</h2>} />
        <Route path="/home" element={<h2>Home Page</h2>} />
      </Routes>
    </BrowserRouter> 
  );
  
}
