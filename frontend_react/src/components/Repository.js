import React from "react"

export default function Repository(repo) {
    return (
    <div className="repo">
        <h3 className="repo--name">{repo.name}</h3>
        <p className="repo--public">{repo.public}</p>
        <p className="repo--update">Last update: {repo.update}</p>
        <p className="repo--coop"> {repo.coop}</p>
        <p className="repo--files">{repo.files} files exist</p>
    </div>
    )
}