import React from 'react'

function PostJobComponent(props){
    return(
            <form>
                <input type = "text" value={props.data.jobid} name = "jobid" placeholder= "JobID" onChange = {props.handleSubmit}>
                </input>
                    <input type = "text" value={props.data.jobtitle} name = "jobtitle" placeholder= "JobTitle" onChange = {props.handleSubmit}>
                    </input>
                        <input type = "text" value={props.data.jobdescription} name = "jobdescription" placeholder= "JobDec" onChange = {props.handleSubmit}>
                        </input>
                <button onClick={props.onSubmit}>Submit</button>
            </form>
    )
}

export default PostJobComponent