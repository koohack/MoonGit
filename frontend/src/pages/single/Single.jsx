import "./single.scss"; 
import Sidebar from "../../components/sidebar/Sidebar"
import Navbar from "../../components/navbar/Navbar"

function Single() {
  return (
    <div className="single">
      <Sidebar />
      <div className="singleContainer">
        <Navbar />
        single
      </div>
    </div>
  )
}

export default Single