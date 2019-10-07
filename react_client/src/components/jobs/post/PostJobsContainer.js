import React from 'react'
import PostJobComponent from "./PostJobsComponent";

class PostJobsContainer extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
        };
        this.onSubmit = this.onSubmit.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    onSubmit(event) {
        this.handleSubmit(event)
        var formBody = [];
        for (var property in this.state) {
            var encodedKey = encodeURIComponent(property);
            var encodedValue = encodeURIComponent(this.state[property]);
            formBody.push(encodedKey + "=" + encodedValue);
        }
        formBody = formBody.join("&");
        console.log('subimt event')

        fetch('http://127.0.0.1:8000/jobs/post', {
            method : 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
            },
            body: formBody
        });

    }

    handleSubmit(event){

        this.setState({
            [event.target.name] : event.target.value,
        }, () => console.log(this.state));

    }



    render() {
        return (

            <form>
                <input type = "text" value={this.state.jobid} name = "jobid" placeholder= "JobID" onChange = {this.handleSubmit}>
                </input>
                <input type = "text" value={this.state.jobtitle} name = "jobtitle" placeholder= "JobTitle" onChange = {this.handleSubmit}>
                </input>
                <input type = "text" value={this.state.jobdescription} name = "jobdescription" placeholder= "JobDec" onChange = {this.handleSubmit}>
                </input>
                <button onClick={this.onSubmit}>Submit</button>
            </form>
        );
    }

}

export default PostJobsContainer