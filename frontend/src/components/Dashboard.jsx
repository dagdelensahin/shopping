import React from 'react'
import { NAV_ITEMS } from '../NavConfig';
import { NavLink } from 'react-router-dom';

function Dashboard() {
    return (
        <nav> 
            <ul> 
                 {NAV_ITEMS.map(({ label, path }) => (
                    <li key={path}>
                        <NavLink to={path}>{label}</NavLink>
                    </li>
                ))}
            </ul>
        </nav>
    );
}

export default Dashboard;