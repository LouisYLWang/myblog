const postAPI =
    "https://ylwang.codes/api/posts/?format=json";

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
    var filtered_posts = postJSON.filter((key) => key.title.toLowerCase().includes(searchKey));
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
                <span class="badge badge-pill badge-info">test</span>
            </div>

            <p class="card-text">${post.excerpt}</p>
            <p id="post-time" class="card-text"><small class="text-muted">${post.created_time}</small></p>
            <a class="btn btn-primary btn-lg btn-block" href=https://ylwang.codes/posts/${post.id} role="button">Read More</a>
        </div>`;
}

function parseAsJSON(response) {
    return response.json()
}

function handleError(err) {
    console.error(err);
    alert(err.message);
}


var postJSON= fetch(postAPI, {
    method: "GET",
    headers: {
        'Access-Control-Allow-Origin': "https://ylwang.codes/api/posts/?format=json",
        'Access-Control-Allow-Credentials': 'true'
    }
}).then(parseAsJSON)
  .then(renderPosts)
  .then(handleError) 

//renderPosts(POST)