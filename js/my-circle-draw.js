var data = [
    {x: 35, y: 35, r: 0},
    {x: 70, y: 70, r: 70},
    {x: 90, y: 70, r: 70},
    {x: 105, y: 115, r: 50}
];

function go() {
    var draw = SVG('drawing').size(300, 130);
    var circle = draw.circle(50).fill('#fff');

    var clip = draw.clip();

    data.forEach (function (e) {
        clip.add(circle.clone().center(e.x, e.y).size(e.r).fill('#ccc'));
    });

    //clip.add(circle.center(35, 35));
    //clip.add(circle.clone().center(70, 70).size(70).fill('#ccc'));
    //clip.add(circle.clone().center(90, 30).size(30).fill('#999'));
    //clip.add(circle.clone().center(105, 115).size(50).fill('#333'));

    var rect = draw.rect(100, 100).move(20, 20).fill('#f06');
    rect.clipWith(clip);

    rect.on('mouseover', function() {
        this.animate(300, '<>').fill('#0f9');
    });
    rect.on('mouseout', function() {
        this.animate(300, '<>').fill('#f06');
    });
}
