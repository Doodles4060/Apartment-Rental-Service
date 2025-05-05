<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const baseUrl = import.meta.env.VITE_API_URL

const apartments = ref([])

// Filters
const filters = ref({
  price_min: null,
  price_max: null,
  rooms: null,
  availability: null,
  search: null,
})

const buildQuery = () => {
  const params = new URLSearchParams()
  if (filters.value.price_min) params.append('price_min', filters.value.price_min)
  if (filters.value.price_max) params.append('price_max', filters.value.price_max)
  if (filters.value.rooms) params.append('rooms', filters.value.rooms)
  if (filters.value.availability !== null) params.append('available', filters.value.availability)
  if (filters.value.search) params.append('search', filters.value.search)
  return params.toString()
}

// Pagination
const nextUrl = ref(null)
const prevUrl = ref(null)
const currentPage = ref(1)
const pageSize = ref(10)
const pageCount = ref(0)

const fetchApartments = async (url = null) => {
  try {
    let finalUrl = url

    // If no full URL passed, build it from base + filters
    if (!url) {
      const query = buildQuery()
      finalUrl = `${baseUrl}/apartments/apartments/?${query}`
    }

    const response = await axios.get(finalUrl)
    apartments.value = response.data.results

    // Get pagination info
    nextUrl.value = response.data.next
    prevUrl.value = response.data.previous
    pageCount.value = Math.ceil(response.data.count / pageSize.value)

    const pageParam = new URL(finalUrl).searchParams.get('page')
    currentPage.value = pageParam ? parseInt(pageParam) : 1
  } catch (error) {
    console.error('Failed to fetch apartments:', error)
  }
}

const applyFilters = () => {
  currentPage.value = 1
  fetchApartments()
}

onMounted(() => {
  fetchApartments()
})
</script>

<template>
  <div>
    <!-- Filters -->
    <form @submit.prevent="applyFilters">
      <input type="number" v-model.number="filters.price_min" placeholder="Min Price" />
      <input type="number" v-model.number="filters.price_max" placeholder="Max Price" />
      <input type="number" v-model.number="filters.rooms" placeholder="Rooms" />
      <select v-model="filters.availability">
        <option :value="null">Any Availability</option>
        <option :value="true">Available</option>
        <option :value="false">Unavailable</option>
      </select>
      <input type="text" v-model="filters.search" placeholder="Search..." />
      <button type="submit">Apply</button>
    </form>

    <!-- Apartment List -->
    <div v-for="apartment in apartments" :key="apartment.slug">
      <div :class="apartment.availability ? 'bg-red-500' : 'bg-green-500'">
        <h2>
          <router-link :to="`/apartment/${apartment.slug}`">{{ apartment.name }}</router-link>
        </h2>
      </div>
    </div>

    <!-- Pagination -->
    <div>
      <button @click="fetchApartments(prevUrl)" :disabled="!prevUrl">←</button>

      <span v-for="i in pageCount" :key="i">
        <span v-if="i === currentPage">
          <strong>{{ i }}</strong>
        </span>
        <span v-else>
          <button
              @click="fetchApartments(`${baseUrl}/apartments/apartments/?page=${i}&${buildQuery()}`)">
            {{ i }}
          </button>
        </span>
      </span>

      <button @click="fetchApartments(nextUrl)" :disabled="!nextUrl">→</button>
    </div>
  </div>
</template>
