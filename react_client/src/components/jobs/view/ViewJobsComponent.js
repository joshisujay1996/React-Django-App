import React from 'react'

function ViewJobsComponent(props){
    if (props.data.isLoading === true){
        return (
            <h1> Loading </h1>
        )
    }
    else {
        return (
            <div>
                <h1>Lodded</h1>
                {/*Need to get jobs induvisually*/}
                {/*{parse_json(props.data.job)}*/}
                <p> {(props.data.job)}</p>
            </div>

        )
    }
}

function parse_json(data){
    console.log(data)
    for(let i = 0; i< data.length; i++){
        let d1 = JSON.parse(JSON.stringify(data[i]))
        console.log(d1)
    }
}
export default ViewJobsComponent