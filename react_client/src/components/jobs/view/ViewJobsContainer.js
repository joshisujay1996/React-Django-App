import React from 'react'
import ViewJobsComponent from "./ViewJobsComponent";

class ViewJobs extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            isLoading : true,
            job : []
        }
    this.setFetchData = this.setFetchData.bind(this)

    }

    setFetchData(data){
        //console.log(data)
        this.setState(
            {
                isLoading: false,
                job : data

            }
            //Need to check the state value using callback functions, its async
            ,() => console.log(this.state))
    };

    componentDidMount() {
        const url = 'http://127.0.0.1:8000/jobs/view'
        fetch('http://127.0.0.1:8000/jobs/view').then(response => response.json()).then(data => data.jobs).then(
            jobs => {
                // console.log(jobs)
                // this.setState({
                //     job:jobs
                // })
            //    Need to set state like above but not working; we need to have a callback function to update
                this.setFetchData(jobs)
            }
        )
    }

//    methonds
    render() {
        return(
            <ViewJobsComponent data = {this.state}/>
        )
    }

}

export default ViewJobs