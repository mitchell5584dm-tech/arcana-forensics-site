/* Meta Pixel: Arcana Forensics */
(function (f, b, e, v, n, t, s) {
  if (f.fbq) return;
  n = f.fbq = function () {
    n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments);
  };
  if (!f._fbq) f._fbq = n;
  n.push = n;
  n.loaded = true;
  n.version = "2.0";
  n.queue = [];
  t = b.createElement(e);
  t.async = true;
  t.src = v;
  s = b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t, s);
})(window, document, "script", "https://connect.facebook.net/en_US/fbevents.js");

fbq("init", "2255314765306462");
fbq("track", "PageView");

document.addEventListener("click", function (event) {
  var link = event.target.closest && event.target.closest('a[href*="buy.stripe.com"]');
  if (!link) return;
  fbq("track", "InitiateCheckout", {
    content_name: (link.textContent || "Arcana Forensics checkout").trim(),
    content_category: "software",
    currency: "USD"
  });
});
