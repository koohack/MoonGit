import "./navbar.scss";
import SearchIcon from '@mui/icons-material/Search';
import LanguageIcon from '@mui/icons-material/Language';
import DarkModeIcon from '@mui/icons-material/DarkMode';
import FullscreenExitIcon from '@mui/icons-material/FullscreenExit';
import NotificationsNoneIcon from '@mui/icons-material/NotificationsNone';
import ChatBubbleOutlineIcon from '@mui/icons-material/ChatBubbleOutline';
import FormatListBulletedIcon from '@mui/icons-material/FormatListBulleted';


function Navbar() {
  return (
    <div className="navbar">
      <div className="wrapper">
        <div className="search">
          <input type="text" placeholder="Search..." />
          <SearchIcon />
        </div>

        <div className="items">
          <div className="item">
            <LanguageIcon className="icon"/>
            English
          </div>
          <div className="item">
            <DarkModeIcon className="icon"/>
          </div>
          <div className="item">
            <FullscreenExitIcon className="icon"/>
          </div>
          <div className="item">
            <NotificationsNoneIcon className="icon"/>
            <div className="counter">1</div>
          </div>
          <div className="item">
            <ChatBubbleOutlineIcon className="icon"/>
            <div className="counter">2</div>
          </div>
          <div className="item">
            <FormatListBulletedIcon className="icon"/>
          </div>
          <div className="item">
            <img 
            src="https://t1.daumcdn.net/friends/prod/editor/dc8b3d02-a15a-4afa-a88b-989cf2a50476.jpg"
            alt=""
            className="avatar"
            />
          </div>

        </div>

      </div>
    </div>
  )
}

export default Navbar