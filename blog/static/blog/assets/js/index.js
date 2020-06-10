const postAPI =
    "http://localhost:8000/api/posts/?format=json";

const POST = [
    {
        "id": 4,
        "title": "phylogenetic newick tree pruning",
        "created_time": "2020-06-10T09:46:25Z",
        "excerpt": "",
        "category": {
            "id": 3,
            "name": "Tedious and buggy"
        },
        "tags": {
            "name": null
        },
        "views": 0,
        "img": "http://127.0.0.1:8000/api/posts/3.png"
    },
    {
        "id": 3,
        "title": "Memomatics - a toy project of data visualization",
        "created_time": "2020-06-10T09:45:42Z",
        "excerpt": "site: https://louisylwang.github.io/Memomatics/\nMemomatics is a toy project for giving a surprise for my girlfriend's birthday. It contains instant message log visualization and photo geographical information visualization. It runs on local client while has a online user interface. \ndependencies: python (jieba, sqlite3, pandas, urllib, requests, PIL.Images/ExifTags), echart 3.7.2, tencent AI Lab nlpemo\n1  instant message log visualization\n1.0 hack WeChat log\n1.1 word cloud\n\n1.2 emotion analysis ",
        "category": {
            "id": 2,
            "name": "Fun but meaningless"
        },
        "tags": {
            "name": null
        },
        "views": 0,
        "img": "http://127.0.0.1:8000/api/posts/step_%E7%9A%84%E5%89%AF%E6%9C%AC_1.png"
    },
    {
        "id": 2,
        "title": "Information Ethic term paper- review of #Why Software Should Be Free#",
        "created_time": "2020-06-10T09:45:03Z",
        "excerpt": "Part I explain of conclusion\nIn Why Software Should Be Free, Richard Stallman mainly aimed to argue that current obstructing proprietary make several undesired overall counter effects, therefore the ecosystem of software should shift to an unrestrictive, nonexclusive and anti-proprietary system of share, distribute and upgrade software. He also insists that every programmer have a justification to support free software. \nIn achieving this conclusion, he firstly presents several arguments from em",
        "category": {
            "id": 1,
            "name": "louis"
        },
        "tags": {
            "name": null
        },
        "views": 0,
        "img": "http://127.0.0.1:8000/api/posts/1_ZCIB1uW.png"
    },
    {
        "id": 1,
        "title": "Sync Sofa - streaming video playback synchronizer extension",
        "created_time": "2020-06-06T08:25:47Z",
        "excerpt": "Sync Sofa - streaming video playback synchronizer extension\n\nThis chrome extension allows multi-user sync streaming video in a fast, simple and stable way.\n\n\n\nSync Sofa is a full stack web extension support a easy-to-use and stable way to synchronize streaming playback for multiple users. It can improve the experience when users from different locations want to share a video/movie remotely. Currently the feartures include:\n\n2 party connection: either party can be the host of a sync room and the ",
        "category": {
            "id": 1,
            "name": "louis"
        },
        "tags": {
            "name": null
        },
        "views": 40,
        "img": "http://127.0.0.1:8000/api/posts/1.png"
    }
]

function renderPosts(post_list) {
    postCardColumns = document.querySelector(".card-columns");
    // don't forget to clear
    postCardColumns.textContent = "";
    post_list.sort((a, b) => b.id - a.id);
    post_list.forEach(post_raw => {
        console.log(post_raw);
        renderPost(post_raw);
    });
}


var search = document.querySelector("#post-filter");
search.addEventListener("input", (e) => {
    e.preventDefault;
    var searchKey = search.value.toLowerCase();
    var filtered_posts = POST.filter((key) => key.title.toLowerCase().includes(searchKey));
    renderPosts(filtered_posts);
})

function renderPost(post) {
    var postToAdd = document.createElement("div");
    postToAdd.setAttribute("class", "card");
    postToAdd.setAttribute("id", `post_${post.id}`);
    console.log(postToAdd);
    postCardColumns = document.querySelector(".card-columns");
    postCardColumns.appendChild(postToAdd);
    console.log(document.getElementById("post_1"));
    document.getElementById(`post_${post.id}`).innerHTML = `
        <img class="card-img-top" src="/static/blog/assets/img/${post.id}.jpg" alt="Card image cap">
        <div class="card-body">
            <h5 class="card-title">${post.title}</h5>
            <div class="read-comment-info">
                <span class="badge badge-success">Read</span>
                <span class="badge badge-pill badge-primary">${post.views}</span>
                <span class="badge badge-warning">Comment</span>
                <span class="badge badge-pill badge-primary">0</span>
            </div>
            <div class="tags">
                <span class="badge badge-pill badge-danger">${post.category.name}</span>
                <span class="badge badge-pill badge-info">Java</span>
                <span class="badge badge-pill badge-info">Project</span>
            </div>

            <p class="card-text">${post.excerpt}</p>
            <p id="post-time" class="card-text"><small class="text-muted">${post.created_time}</small></p>
            <a class="btn btn-primary btn-lg btn-block" href=http://127.0.0.1:8000/posts/${post.id} role="button">Read More</a>
        </div>`;
}

function parseAsJSON(response) {
    return response.json()
}

function handleError(err) {
    console.error(err);
    alert(err.message);
}

/*
var postJSON= fetch(postAPI, {
    method: "GET",
    headers: {
        'Access-Control-Allow-Origin': "http://localhost:8000/api/posts/?format=json",
        'Access-Control-Allow-Credentials': 'true'
    }
})
.then(parseAsJSON)
  .then(renderPosts)
  .then(handleError) */

renderPosts(POST)