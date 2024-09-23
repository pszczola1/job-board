const fetchListings = async (isInitial=false, filters=[]) => {
    let pageNumber = (new URLSearchParams(window.location.search)).get("page")
    let testNumRegex = /^\d+$/m
    if(!testNumRegex.test(pageNumber)) pageNumber = 1

    let response
    if(isInitial) response = await fetch(`${window.location.origin}/api/v1/listings/?page=${pageNumber}`)
    else {
        let apiUrl = `${window.location.origin}/api/v1/listings/?page=${pageNumber}`
        for (const filter of filters) {
            apiUrl += `&${filter[0]}=${filter[1]}`
        }
        response = await fetch(apiUrl)
    }
    return response.json()
}


const buildPage = (listings) => { 
    const listingsDiv = document.querySelector('.listings')
    for (const listing of listings) {
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
        salarySpan.innerText = listing.salary

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
}

const clearPage = () => {
    const listingsWrapper = document.querySelector(".listings")
    listingsWrapper.innerHTML = ""
}


const main = async () => {
    const response = await fetchListings(isInitial=true)
    buildPage(response.results)
    const filterBtn = document.querySelector(".filter-submit-btn")
    filterBtn.addEventListener("click", handleFilterBtn)
}

const handleFilterBtn = async (e) => {
    e.preventDefault()
    const formData = getFilterFormData()
    let filters = []
    for (const element of formData.entries()) {
        if(element[1] == "") continue
        filters.push([element[0], element[1]])
    }
    const response = await fetchListings(isInitial=false, filters=filters)
    clearPage()
    buildPage(response.results)
}

const getFilterFormData = () => {
    const form = document.querySelector(".filter-form")
    const formData = new FormData(form)
    return formData
}

window.addEventListener("DOMContentLoaded", main)