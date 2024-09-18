const fetchListings = async () => {
    const pageNumber = (new URLSearchParams(window.location.search)).get("page")
    
    const response = await fetch(`${window.location.origin}/api/v1/listings/?page=${pageNumber}`)
    const listings = await response.json()
    return listings   
}


window.addEventListener("DOMContentLoaded", async () => {
    response = await fetchListings()
    const listingsDiv = document.querySelector('.listings')
    for (const listing of response.results) {
        //console.log(listing)
        let listingWrapper = document.createElement('div')
        listingWrapper.classList.add('listing')
        const title = listing.title
        let categories = []
        for (const category of listing.categories) {
            categories.push(category.name)
        }
        const offeredPay = listing.offered_pay
        let listingAnchorTag = document.createElement('a')
        listingAnchorTag.href = `${window.location.origin}/listing/${listing.pk}`
        listingAnchorTag.innerText = `${title} ${categories} ${offeredPay}`

        listingWrapper.appendChild(listingAnchorTag)
        listingsDiv.appendChild(listingWrapper)
    }
})