import React from 'react';
import Home from '../home/Home'
import ViewJobs from '../jobs/view/ViewJobsContainer'
import PostJobsContainer from '../jobs/post/PostJobsContainer'
// import ReactDOM from 'react-dom'
import { Route, Link, BrowserRouter as Router } from 'react-router-dom'

class NavBarTemplate extends React.Component {

    constructor(props) {
        super(props);
        this.state = {

        };
    }

    render() {
        return (
            <Router>
                <div>
                    <ul>
                        <li>
                            <Link to="/">Home</Link>
                        </li>
                        <li>
                            <Link to="/jobs/view">JobsView</Link>
                        </li>
                        <li>
                            <Link to="/jobs/post">JobsPost</Link>
                        </li>
                    </ul>
                    <Route exact path="/" component={Home} />
                    <Route exact path="/jobs/view" component={ViewJobs} />
                    <Route exact path="/jobs/post" component={PostJobsContainer} />
                </div>
            </Router>
        );
    }
}

export default NavBarTemplate;