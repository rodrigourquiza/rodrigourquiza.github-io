function userLookup(user, domain) {
    switch(user) {
        case "tracy":
            switch(domain) {
                case "hotmail":
                    return "trmann70"
                case "RBS":
                    return "tracy.mann1"
                case "BYUI":
                    return "man22057"
                default:
                    return "undefined"
            }
        case "luchonio":
            switch(domain) {
                case "hotmail":
                    return "???"
                default:
                    return "undefined"
            }
        default:
            return "undefined"
    }
}
    
function domainLookup(domain) {
    switch(domain) {
        case "hotmail":
            return "hotmail.com"
        case "RBS":
            return "retailbusinessservices.com"
        case "BYUI":
            return "byui.edu"
        default:
            return "undefined"
    }
}
    
function emailLookup(user, domain) {
    return userLookup(user) + "@" + domainLookup(domain)
}
    
//mailToLink("contact-me-link", "tracy", "RBS", "E-Mail Me")
function mailToLink(linkClass, user, domain, content) {
    document.write('<a class=\"' + linkClass + '\" href=\"mailto:' + emailLookup(user, domain) + '\" target="_blank">' + content + '</a>');
}
    
//mailToLink("contact-me-link", "contact-me-icon", "luchonio", "hotmail", "images/luchonio_logo.png", "Luchonio Logo")
function mailToImgLink(linkClass, imgClass, user, domain, imgSource, imgAlt) {
    mailToLink(linkClass, user, domain, '<img class="' + imgClass + '" src=\"' + imgSource + '\" alt=\"' + imgAlt + '\">');
}
    
function countryCodeLookup(phone) {
    switch(phone) {
        case "tracy":
            return "1"
        case "luchonio":
            return "??"
        default:
            return "1"
    }
}
    
function areaCodeLookup(phone) {
    switch(phone) {
        case "tracy":
            return "864"
        case "luchonio":
            return "???"
        default:
            return "000"
    }
}
    
function basePhoneNumberLookup(phone) {
    switch(phone) {
        case "tracy":
            return "0724"
        case "luchonio":
            return "????????"
        default:
            return "0000"
    }
}
    
function phoneLookup(phone) {
    return countryCodeLookup(phone) + areaCodeLookup(phone) + basePhoneNumberLookup(phone)
}
    
//messageWhatsAppLink("whatsApp-me-link", areaCode + phone, "Call20%Me!", "What's App Me")
function messageWhatsAppLink(linkClass, phone, message, content) {
    if(phone == "") {
        document.write('<a class=\"' + linkClass + '\" href=\"https://www.whatsapp.com/\" target="_blank">' + content + '</a>');
    } else {
        document.write('<a class=\"' + linkClass + '\" href=\"https://api.whatsapp.com/send?phone=' + phoneLookup(phone) + '&text=' + message + '\" target="_blank">' + content + '</a>');
    };
}
    
//messageWhatsAppImgLink("whats-app-me-link", "whats-app-me-icon", "tracy", "Call20%Me!", "images/whatsapp.png", "What's App Icon")
function messageWhatsAppImgLink(linkClass, imgClass, phone, message, imgSource, imgAlt) {
    messageWhatsAppLink(linkClass, phone, message, '<img class="' + imgClass + '" src=\"' + imgSource + '\" alt=\"' + imgAlt + '\">');
}

function toUseLaterForMobileVrsLargeScreenJavaScriptoptions(){
    if (window.matchMedia("(max-width: 700px)").matches) {
        // Viewport is less or equal to 700 pixels wide
      } else {
        // Viewport is greater than 700 pixels wide
      }

//      in conjunctioned with css as follows:

//      @media screen and (max-width: 992px) {
//        .column {
//          width: 50%;
//        }
//      }

//       "Mobile Navigation Bar" - https://www.w3schools.com/howto/howto_js_mobile_navbar.asp


}
