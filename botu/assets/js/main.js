const recordUrl1 = "http://www.k-sok.com/corunners/timeline?raceId=5617";

async function getDom(url){
    return await fetch(url,{mode: "no-cors"})
    .then(res => res.text())
    .then(text => new DOMParser().parseFromString(text,"text/html"));
}

window.addEventListener("load", async event => {
    console.log("onLoad");
    const dom = await getDom(recordUrl1);
    console.log(dom);  
});