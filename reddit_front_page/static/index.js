$(document).ready(function() {{
    localStorage.getItem('RedditFrontPage') === 'dark' ? setDark() : setLight();
}});

function setDark() {{
    localStorage.setItem('RedditFrontPage', 'dark');
    document.documentElement.setAttribute('data-theme', localStorage.getItem('RedditFrontPage'));
    $('#dark').show();
    $('#light').hide();
}}

function setLight() {{
    localStorage.setItem('RedditFrontPage', 'light');
    document.documentElement.setAttribute('data-theme', localStorage.getItem('RedditFrontPage'));
    $('#light').show();
    $('#dark').hide();
}}

function toggleDiv(divId) {
    $('#' + divId).fadeToggle(150);
}

function getPosts(displayName) {
    $('#spinner').show();
    $.get('get_posts', {
        display_name: displayName
    }, function (data) {
        $('#posts').html('');
        $('#posts').append(`<p class="text-center font-custom">${displayName}</p>`);
        for (x of data.posts) {
            $('#posts').append(`
                <a class="row text-truncate" href="${x.url}" target="blank_">
                <span class="col-1 font-custom"><i class="bi bi-arrow-down-up"></i> ${x.score}</span>
                <span class="col-9 text-truncate fw-bold">${x.title}</span>
                <span class="col-2 fw-light text-muted">${x.created_utc}</span>
                </a>`);
        }
        $('#spinner').hide();
    });
}
