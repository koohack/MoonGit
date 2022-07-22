import "./sidebar.scss";
import DashboardIcon from '@mui/icons-material/Dashboard';
import ImportContactsIcon from '@mui/icons-material/ImportContacts';
import BookIcon from '@mui/icons-material/Book';
import NotificationsIcon from '@mui/icons-material/Notifications';
import SettingsIcon from '@mui/icons-material/Settings';
import PersonIcon from '@mui/icons-material/Person';

function Sidebar() {
  return (
    <div className='sidebar'>
        <div className="top">
            <span className="logo">
                MoonGit
            </span>
        </div>
        
        
        <div className="center">
            <ul>
                <p className="title">MAIN</p>
                <li>
                    <DashboardIcon className="icon" />
                    <span>Dashboard</span>
                </li>
                <li>
                    <ImportContactsIcon className="icon" />
                    <span>Overview</span>
                </li>
                <li>
                    <BookIcon className="icon" />
                    <span>Repositories</span>
                </li>
                <li>
                    <NotificationsIcon className="icon" />
                    <span>Issues</span>
                </li>
                <p className="title">SERVICE</p>
                <li>
                    <PersonIcon className="icon" />
                    <span>Profile</span>
                </li>
                <li>
                    <SettingsIcon className="icon" />
                    <span>Setting</span>
                </li>
                
            </ul>
        </div>
        
        <div className="buttom">color option</div>
    </div>
  )
}

export default Sidebar