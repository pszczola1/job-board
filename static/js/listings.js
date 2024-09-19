const fetchListings = async () => {
    let pageNumber = (new URLSearchParams(window.location.search)).get("page")
    
    let testNumRegex = /^\d+$/m
    if(!testNumRegex.test(pageNumber)) pageNumber = 1
     
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

        let imgWrapper = document.createElement('div')
        imgWrapper.classList.add('image-wrapper')
        //let img = new Image() //TODO
        //imgWrapper.appendChild(img)

        let textWrapper = document.createElement('div')
        textWrapper.classList.add('text-wrapper')

        let categories = []
        for (const category of listing.categories) {
            categories.push(category.name)
        }
        let titleSpan = document.createElement('span')
        titleSpan.classList.add('title-span')
        titleSpan.innerText = listing.title

        let categoriesSpan = document.createElement('span')
        categoriesSpan.classList.add('categories-span')
        categoriesSpan.innerText = "Categories: " + categories.toString()

        let salarySpan = document.createElement('span')
        salarySpan.classList.add('salary-span')
        salarySpan.innerText = listing.offered_pay

        textWrapper.appendChild(titleSpan)
        textWrapper.appendChild(salarySpan)
        textWrapper.appendChild(categoriesSpan)

        listingWrapper.appendChild(imgWrapper)
        listingWrapper.appendChild(textWrapper)
        listingWrapper.addEventListener("click", () => {
            window.location.href = window.location.origin + "/listing/" + listing.pk
        })
        listingsDiv.appendChild(listingWrapper)
    }
})