let pageNumber = 1

const fetchListings = async (filters=[], apiUrl=null) => {
    if(!apiUrl) apiUrl = `${window.location.origin}/api/v1/listings/?page=${pageNumber}`
    for (const filter of filters) {
        apiUrl += `&${filter[0]}=${filter[1]}`
    }
    console.log(filters, apiUrl);
    
    const response = await fetch(apiUrl)
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
    const pageBtns = document.querySelector(".change-page-btns")
    pageBtns.innerHTML = ""
}


const init = async () => {
    const response = await fetchListings()
    console.log(response);
    
    buildPage(response.results)
    buildPageBtns(response.previous, response.next)
    const filterBtn = document.querySelector(".filter-submit-btn")
    filterBtn.addEventListener("click", handleFilterBtn)
}

window.addEventListener("DOMContentLoaded", init)

const handleFilter = async (filters) => {
    const response = await fetchListings(filters=filters)  
    clearPage()
    buildPage(response.results)
    buildPageBtns(response.previous, response.next)
}

const handleFilterBtn = async (e) => {
    e.preventDefault()
    const formData = getFilterFormData()
    let filters = []
    for (const element of formData.entries()) {
        if(element[1] == "") continue
        filters.push([element[0], element[1]])
    }
    handleFilter(filters)
}

const getFilterFormData = () => {
    const form = document.querySelector(".filter-form")
    const formData = new FormData(form)
    return formData
}

const buildPageBtns = (previous, next) => {
    const btnsDiv = document.querySelector(".change-page-btns")
    if (previous) {
        const previousBtn = document.createElement("button")
        previousBtn.innerText = "<"
        previousBtn.addEventListener("click", () => {handlePageChange(previous)})
        btnsDiv.appendChild(previousBtn)
    }

    if (next) {
        const nextBtn = document.createElement("button")
        nextBtn.innerText = ">"
        nextBtn.addEventListener("click", () => {handlePageChange(next)})
        btnsDiv.appendChild(nextBtn)
    }

}

const handlePageChange = async (apiUrl) => {
    const response = await fetchListings(filters=[], apiUrl=apiUrl)
    clearPage()
    buildPage(response.results)
    buildPageBtns(response.previous, response.next)
}