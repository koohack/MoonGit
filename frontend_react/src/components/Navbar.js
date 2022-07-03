import React from "react"
import logo from '../images/moonLogo2.png';

export default function Navbar() {
    return (
        <nav>
            <img src={logo} alt="Logo" className="nav--icon"/>
            <h3 className="nav--menu">Profile</h3>
            <h3 className="nav--menu">Overview</h3>
            <h3 className="nav--menu">Repository</h3>
            <h3 className="nav--menu">Issues</h3>
        </nav>
    )
}