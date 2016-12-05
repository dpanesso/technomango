/**
 * Created by David Panesso on 24/11/16.
 * Credits to Eric Saupe
 * http://eric.sau.pe/simple-javascript-clock-with-time-zone-support/
 */


function startTime(element_id, dst, offset) {
    //Extra functionality for Date to calculate DST
    Date.prototype.stdTimezoneOffset = function () {
        var jan = new Date(this.getFullYear(), 0, 1);
        var jul = new Date(this.getFullYear(), 6, 1);
        return Math.max(jan.getTimezoneOffset(), jul.getTimezoneOffset());
    };
    Date.prototype.dst = function () {
        return this.getTimezoneOffset() < this.stdTimezoneOffset();
    };

    var now = new Date();
    //Calculate Daylight Savings time in areas where that matters
    if (dst) {
        if (now.dst()) {
            offset += 1;
        }
    }
    var today = new Date(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate(), now.getUTCHours() + offset, now.getUTCMinutes(), now.getUTCSeconds());
    var h = today.getHours();
    var m = today.getMinutes();
    // add a zero in front of numbers<10
    m = checkTime(m);
    var clock = document.getElementById(element_id);
    if (clock != null) {
        clock.innerHTML = h + ":" + m;
        var t = setTimeout(function () {
            startTime(element_id, dst, offset)
        }, 500);
    }
}

function checkTime(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
}