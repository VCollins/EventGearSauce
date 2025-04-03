import { NavLink } from "react-router-dom";
import "../styles/NavBar.css";

function NavBar() {
    return <div className="navbar">
        <div className="navmenu">
            <NavLink className="navlink" to="/">Home</NavLink>
            <NavLink className="navlink" to="/about">About Us</NavLink>
            <NavLink className="navlink" to="/contact">Contact Us</NavLink>
            <NavLink className="navlink" to="/login">Login</NavLink>
            <NavLink className="navlink" to="/register">Register</NavLink>
        </div>
    </div>
}

export default NavBar