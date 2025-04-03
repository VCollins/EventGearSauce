import "../styles/NavBar.css"

function NavBar() {
    return <div className="navbar">
        <div className="navmenu">
            <a className="navlink" to="/">Home</a>
            <a className="navlink" to="/about">About Us</a>
            <a className="navlink" to="/contact">Contact Us</a>
            <a className="navlink" to="/login">Login</a>
            <a className="navlink" to="/register">Register</a>
        </div>
    </div>
}

export default NavBar