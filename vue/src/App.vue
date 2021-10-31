<template>
  <div>
    <!-- Nav bar -->
    <nav class="navbar navbar-expand navbar-light bg-light">
      <div class="container">
        <a class="navbar-brand float-left " href="/">Student Management App</a>
        <ul class="nav navbar-nav mr-auto" >
          <li class="nav-item">
            <router-link class="nav-link" to="/create">Sign Up For Distribution</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/view">View Events</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/graph">graph</router-link>
          </li>
        </ul>
      </div>
    </nav>
    <!-- Router view -->
    <div class="container mt-5">
      <router-view></router-view>
    </div>
  </div>
</template>
