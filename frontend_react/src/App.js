import React from "react"
import Navbar from "./components/Navbar"
import Repository from "./components/Repository"
import RepositoryAdd from "./components/RepositoryAdd"

export default function App() {
    return (
        <div className="container">
            <Navbar />
            <Repository
                name="Repository 1"
                public="Public"
                update="2022/02/04"
                coop="Hong-Gil-Dong"
                files="2"
            />
            <Repository
                name="Repository 2"
                public="Private"
                update="2022/02/06"
                coop="Kim-Cheol-Su"
                files="4"
            />
            <Repository
                name="Repository 3"
                public="Private"
                update="2022/02/08"
                coop="Hong-Gil-Dong"
                files="3"
            />
            <Repository
                name="Repository 4"
                public="Public"
                update="2022/02/10"
                coop="Kim-Cheol-Su"
                files="1"
            />
            <RepositoryAdd />
        </div>
    )
}